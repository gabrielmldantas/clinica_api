"""Criacao da tabela especialidade

Revision ID: 73ed255af28f
Revises: 
Create Date: 2020-05-06 20:08:07.320767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73ed255af28f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('especialidade',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.Unicode(length=80), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descricao')
    )


def downgrade():
    op.drop_table('especialidade')
