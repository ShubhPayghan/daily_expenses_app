from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '2345bcde6789'
down_revision = '1234abcd5678'
branch_labels = None
depends_on = None

def upgrade():
    # Add any new columns or tables here
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))

def downgrade():
    # Drop any new columns or tables here
    op.drop_column('user', 'password_hash')
