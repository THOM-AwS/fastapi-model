"""create posts table

Revision ID: 5c957e3155f4
Revises: 
Create Date: 2021-12-30 20:26:56.443998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c957e3155f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer, nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass
