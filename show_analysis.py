from io import BytesIO
from flask import Flask, render_template, send_file, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from tweets_analyzer import analyze, plot_graphs
import matplotlib.pyplot as plt
plt.style.use('ggplot')

app = Flask(__name__)

@app.route('/')
def index():
    analysis_details = analyze()
    fans_by_housemate, fans_by_location, followers_of_fans_by_hm = analysis_details
    fans_by_location_table = fans_by_location.pivot_table(index='location', columns='housemate_name', values='count')

    return render_template("index.html", fans_by_housemate_df=fans_by_housemate.to_html(), 
    followers_of_fans_by_hm_df=followers_of_fans_by_hm.to_html(), fans_by_location_df=fans_by_location_table.to_html())

@app.route('/fans_by_hm_bar_chart/')
def fans_by_hm_bar_chart():
    figures = plot_graphs()
    fig1 = figures[0]
    canvas = FigureCanvas(fig1)
    img = BytesIO()
    fig1.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

@app.route('/fans_by_location_bar_chart/')
def fans_by_location_bar_chart():
    figures = plot_graphs()
    fig2 = figures[1]
    canvas = FigureCanvas(fig2)
    img = BytesIO()
    fig2.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run()