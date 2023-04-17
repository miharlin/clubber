"""add grade to User

Revision ID: 105e2b54e6e7
Revises: ec0cf192fa35
Create Date: 2023-04-17 15:33:12.997227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '105e2b54e6e7'
down_revision = 'ec0cf192fa35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('grade', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'grade')
    # ### end Alembic commands ###
