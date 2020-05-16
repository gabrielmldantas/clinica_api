"""Criacao da tabela usuario

Revision ID: 7e0e834e6151
Revises: 1711fd668191
Create Date: 2020-05-13 16:27:47.070158

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e0e834e6151'
down_revision = '1711fd668191'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('usuario',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('username', sa.String(length=30), nullable=False),
        sa.Column('email', sa.String(length=80), nullable=False),
        sa.Column('senha', sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('usuario')
