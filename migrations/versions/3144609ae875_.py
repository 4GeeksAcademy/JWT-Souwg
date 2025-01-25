"""empty message

Revision ID: 3144609ae875
Revises: 03a30a629ed2
Create Date: 2025-01-25 20:15:04.138898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3144609ae875'
down_revision = '03a30a629ed2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blocked_token_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('jti')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blocked_token_list')
    # ### end Alembic commands ###
