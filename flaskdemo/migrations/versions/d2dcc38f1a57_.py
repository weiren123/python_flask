"""empty message

Revision ID: d2dcc38f1a57
Revises: 92bff5232730
Create Date: 2018-04-23 09:54:02.242636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2dcc38f1a57'
down_revision = '92bff5232730'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthday', sa.String(length=100), nullable=False))
    op.add_column('user', sa.Column('userbgimg', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'userbgimg')
    op.drop_column('user', 'birthday')
    # ### end Alembic commands ###
