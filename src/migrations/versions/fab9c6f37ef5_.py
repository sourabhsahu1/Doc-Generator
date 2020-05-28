"""empty message

Revision ID: fab9c6f37ef5
Revises: c3721bca540b
Create Date: 2020-05-28 12:44:57.744542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fab9c6f37ef5'
down_revision = 'c3721bca540b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('queuemanager', sa.Column('long_doc_url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('queuemanager', 'long_doc_url')
    # ### end Alembic commands ###
