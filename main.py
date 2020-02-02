from flask import Flask
from flask import jsonify
import pandas as pd
import wikipedia
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello I like to make AI Apps'

@app.route('/graph')
def plotting():
    # Read in dataset from github
    gtdUS = pd.read_csv('./gtdUS.csv',encoding = "ISO-8859-1")

    # Determine number of attacks
    gtdUSincidents = gtdUS.groupby('iyear').count()['city']
    gtdUSincidents = pd.DataFrame(gtdUSincidents)
    gtdUSincidents = gtdUSincidents.reset_index()
    gtdUSincidents.columns = ['Year', 'Attacks']

    # Plot the number of attacks
    fig = px.line(gtdUSincidents, x="Year", y="Attacks")
    fig.update_layout(
        title="Number of Terrorist Attacks in the United States (1970-2017)",
        xaxis_title="Year",
        yaxis_title="Attacks",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
            )
            )

    return pio.write_html(fig, file='index.html', auto_open=True)

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/bob')
def bob():
    val = {"value": "bob"}
    return jsonify(val)

@app.route('/html')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <p>Hello</p>
    <p><b>World</b></p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

@app.route('/wikipedia/<company>')
def wikipedia_route(company):
    # Imports the Google Cloud client library
    from google.cloud import language
    from google.cloud.language import enums
    from google.cloud.language import types
    result = wikipedia.summary(company, sentences=10)

    client = language.LanguageServiceClient()
    document = types.Document(
        content=result,
        type=enums.Document.Type.PLAIN_TEXT)
    entities = client.analyze_entities(document).entities
    return str(entities)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)