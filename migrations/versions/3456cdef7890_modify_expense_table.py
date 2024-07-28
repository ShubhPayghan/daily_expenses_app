from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '3456cdef7890'
down_revision = '2345bcde6789'
branch_labels = None
depends_on = None

def upgrade():
    # Modify the expense table to include a new column
    op.add_column('expense', sa.Column('date', sa.DateTime(), nullable=False, server_default=sa.func.now()))

def downgrade():
    # Drop the new column
    op.drop_column('expense', 'date')
