"""add content column to posts table

Revision ID: bddaa55e30a2
Revises: 5c957e3155f4
Create Date: 2021-12-30 20:37:54.279636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bddaa55e30a2'
down_revision = '5c957e3155f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
