import logging
import pytest
from _pytest.logging import caplog as _caplog
from loguru import logger

#Propagate loguru logs to logger so that we can test logs content with caplog
@pytest.fixture
def caplog(_caplog):
    class PropogateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)
    handler_id = logger.add(PropogateHandler(), format="{message} {extra}")
    yield _caplog
    logger.remove(handler_id)