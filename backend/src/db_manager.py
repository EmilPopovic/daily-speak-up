import os
import sys
import logging
from sqlalchemy import MetaData
from .db import engine, Base

logger = logging.getLogger(__name__)

def drop_all_tables():
    """Drop all database tables"""
    from . import models  # noqa: F401
    
    try:
        logger.warning('Dropping all database tables...')
        
        meta = MetaData()
        meta.reflect(bind=engine)
        meta.drop_all(bind=engine)
        
        Base.metadata.drop_all(bind=engine)
        
        logger.info('All tables dropped successfully!')
    except Exception as e:
        logger.error(f'Failed to drop tables: {e}')
        raise

def create_all_tables():
    """Create all database tables"""
    from . import models  # noqa: F401
    
    try:
        logger.info('Creating all database tables...')
        logger.info(f'Registered tables: {list(Base.metadata.tables.keys())}')
        
        Base.metadata.create_all(bind=engine)
        logger.info('All tables created successfully!')

        logger.info('Created tables:')
        for table_name in Base.metadata.tables.keys():
            logger.info(f'  - {table_name}')

    except Exception as e:
        logger.error(f'Failed to create tables: {e}')
        raise

def reset_database(force: bool = False):
    """Drop all tables and recreate them
    
    Args:
        force: If True, skip confirmation prompt
    """
    env = os.getenv('ENVIRONMENT', 'production').lower()
    if env == 'production' and not force:
        logger.error('Cannot reset database in production environment!')
        raise RuntimeError('Database reset blocked in production')
    
    if not force:
        logger.warning('WARNING: This will DELETE ALL DATA in the database!')
        confirmation = input('Type "yes" to confirm: ')
        if confirmation.lower() != 'yes':
            logger.info('Database reset cancelled')
            return
    
    drop_all_tables()
    create_all_tables()
    logger.info('Database reset complete!')

def main():
    """CLI entry point for database management"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'create':
            create_all_tables()
        elif command == 'drop':
            drop_all_tables()
        elif command == 'reset':
            force = '--force' in sys.argv
            reset_database(force=force)
        else:
            print('Usage:')
            print('  python -m backend.src.db_manager create          # Create all tables')
            print('  python -m backend.src.db_manager drop            # Drop all tables')
            print('  python -m backend.src.db_manager reset           # Drop and recreate (with confirmation)')
            print('  python -m backend.src.db_manager reset --force   # Drop and recreate (no confirmation)')
            sys.exit(1)
    else:
        create_all_tables()

if __name__ == '__main__':
    main()
