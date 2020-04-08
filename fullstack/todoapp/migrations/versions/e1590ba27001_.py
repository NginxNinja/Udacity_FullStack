"""empty message

Revision ID: e1590ba27001
Revises: 06ed814d7b97
Create Date: 2020-04-08 00:13:58.888278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1590ba27001'
down_revision = '06ed814d7b97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todo', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todo', 'todolist', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todo', type_='foreignkey')
    op.drop_column('todo', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###
