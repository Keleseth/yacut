from flask import (
    render_template,
    redirect
)

from . import app, db
from yacut.forms import LinkKnitForm
from yacut.models import URLMap
from yacut.utils import link_links


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkKnitForm()
    if form.validate_on_submit():
        original = form.original_link.data
        short = form.custom_id.data
        urlmap_obj, short = link_links(
            URLMap, original, short
        )
        db.session.add(urlmap_obj)
        db.session.commit()
        return render_template(
            'index.html',
            form=form,
            short=short
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_to_original(short_id):
    urlmap_obj = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(urlmap_obj.original)