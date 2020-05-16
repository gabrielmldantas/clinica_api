"""Criacao das tabelas paciente e endereco

Revision ID: 54ac2f496f4b
Revises: 03b40a1c609a
Create Date: 2020-05-13 12:00:15.160288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54ac2f496f4b'
down_revision = '03b40a1c609a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('endereco',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('rua', sa.String(length=150), nullable=False),
        sa.Column('bairro', sa.String(length=80), nullable=False),
        sa.Column('numero', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('paciente',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('data_nascimento', sa.Date(), nullable=False),
        sa.Column('telefone', sa.Integer(), nullable=False),
        sa.Column('rg', sa.String(length=8), nullable=False),
        sa.Column('cpf', sa.String(length=11), nullable=False),
        sa.Column('id_endereco', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_endereco'], ['endereco.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('paciente')
    op.drop_table('endereco')
