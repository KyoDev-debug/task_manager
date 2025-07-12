from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    title = StringField('タイトル', validators=[DataRequired()])
    status = SelectField('ステータス', choices=[('未着手', '未着手'), ('進行中', '進行中'), ('完了', '完了')])
    deadline = StringField('期限')
    submit = SubmitField('登録')