from flask import (
    render_template,
    redirect
)

from . import app
from yacut.exceptions import ShortLinkAlreadyExists
from yacut.forms import LinkKnitForm
from yacut.models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = LinkKnitForm()
    if form.validate_on_submit():
        data_for_model = {
            'original': form.original_link.data,
            'short': form.custom_id.data
        }
        try:
            urlmap_object = URLMap.link_object_create(data_for_model)
        except ShortLinkAlreadyExists as error:
            form.custom_id.errors.append(error.message)
            return render_template(
                'index.html',
                form=form
            )
        return render_template(
            'index.html',
            form=form,
            short=urlmap_object.short
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_to_original(short_id):
    urlmap_obj = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(urlmap_obj.original)