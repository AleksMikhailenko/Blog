"""followers

Revision ID: 158340479db8
Revises: ced9e7d5fcee
Create Date: 2020-02-03 20:32:09.796315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '158340479db8'
down_revision = 'ced9e7d5fcee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###