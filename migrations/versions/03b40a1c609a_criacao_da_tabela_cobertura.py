"""Criacao da tabela cobertura

Revision ID: 03b40a1c609a
Revises: d8824492fc1e
Create Date: 2020-05-13 10:32:59.079959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b40a1c609a'
down_revision = 'd8824492fc1e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('cobertura',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('descricao')
    )


def downgrade():
    op.drop_table('cobertura')
