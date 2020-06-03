"""Requisicoes

Revision ID: 20977383b6c5
Revises: 75b5ffe8b348
Create Date: 2020-06-03 12:46:34.545811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20977383b6c5'
down_revision = '75b5ffe8b348'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('receita_medica',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.Text(), nullable=False),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('id_consulta', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_consulta'], ['consulta.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('requisicao_exames',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('descricao', sa.Text(), nullable=False),
        sa.Column('data', sa.Date(), nullable=False),
        sa.Column('id_consulta', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_consulta'], ['consulta.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('requisicao_exames')
    op.drop_table('receita_medica')
