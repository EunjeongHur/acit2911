"""empty message

Revision ID: ffa264099fa6
Revises: 
Create Date: 2022-05-17 08:54:43.500320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffa264099fa6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=9), nullable=False),
    sa.Column('class_name', sa.Text(), nullable=False),
    sa.Column('class_credit', sa.Float(), nullable=False),
    sa.Column('grade', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.String(length=9), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('pwd', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pwd'),
    sa.UniqueConstraint('student_id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('course')
    # ### end Alembic commands ###