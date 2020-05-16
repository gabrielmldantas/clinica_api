"""Criacao da tabela medico

Revision ID: d8824492fc1e
Revises: 73ed255af28f
Create Date: 2020-05-13 01:05:49.113295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8824492fc1e'
down_revision = '73ed255af28f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('medico',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('crm', sa.String(length=10), nullable=False),
        sa.Column('id_especialidade', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_especialidade'], ['especialidade.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('medico')
