from flask import render_template,redirect, url_for
from flask_login import current_user,login_required
from . import main
from .forms import PitchForm,CommentForm
from app.models import Post,Comment,Upvote,Downvote

@main.route("/",methods=["GET","POST"])
def index():
    categories=["pickup lines", "interview pitch", "product pitch", "promotion pitch"]
    return render_template('index.html',categories=categories)

@main.route("/pitches/<string:category>")
def pitches(category):
    pitches=Post.query.filter_by(category=category)
    return render_template("./main/pitches.html",pitches=pitches)

@main.route("/pitch/<int:pitch_id>",methods=["GET","POST"])
def pitch(pitch_id):
    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        comment=Comment(
            user_id=current_user.id,
            post_id=pitch_id,
            text=comment_form.comment.data
        )
        comment.save()
    comments=Comment.query.filter_by(post_id=pitch_id)
    pitch=Post.query.filter_by(id=pitch_id).first()
    context={"pitch":pitch,"comments":comments,"comment_form":comment_form}
    return render_template("./main/pitch.html",**context)

@main.route("/add_pitch",methods=["GET","POST"])
@login_required
def add_pitch():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        print(pitch_form.category.data)
        pitch=Post(
            title=pitch_form.title.data,
            text=pitch_form.pitch.data,
            category=pitch_form.category.data,
            user_id=current_user.id,
        )
        pitch.save()
        return redirect(url_for("main.index"))
    return render_template('./main/add_pitch.html',pitch_form=pitch_form)


@main.route("/pitch/upvote/<int:pitch_id>")
@login_required
def upvote(pitch_id):
    upvote_=Upvote.query.filter_by(user_id=current_user.id,post_id=pitch_id).first()
    if not upvote_:
        upvote_=Upvote(user_id=current_user.id,post_id=pitch_id)
        upvote_.save()
    else:
        upvote_.delete_()
    return redirect(url_for("main.pitch",pitch_id=pitch_id))


@main.route("/pitch/downvote/<int:pitch_id>")
@login_required
def downvote(pitch_id):
    downvote_=Downvote.query.filter_by(user_id=current_user.id,post_id=pitch_id).first()
    if not downvote_:
        downvote_=Downvote(user_id=current_user.id,post_id=pitch_id)
        downvote_.save()
    else:
        downvote_.delete_()
    return redirect(url_for("main.pitch",pitch_id=pitch_id))