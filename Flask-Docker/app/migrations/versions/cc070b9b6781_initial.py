"""initial

Revision ID: cc070b9b6781
Revises: 
Create Date: 2021-05-19 14:42:55.385147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc070b9b6781'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_advertisement_name', table_name='advertisement')
    op.drop_table('advertisement')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('advertisement',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_data', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('owner', sa.VARCHAR(length=64), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='advertisement_pkey')
    )
    op.create_index('ix_advertisement_name', 'advertisement', ['name'], unique=False)
    # ### end Alembic commands ###
