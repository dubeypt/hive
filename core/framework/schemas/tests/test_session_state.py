import sys
sys.path.insert(0, "core")

from datetime import datetime
from framework.schemas.session_state import SessionState, SessionStatus

def make_session(status):
    return SessionState(
        session_id="test",
        goal_id="test",
        status=status,
        timestamps={
            "started_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
    )

def test_cancelled_not_resumable():
    s = make_session(SessionStatus.CANCELLED)
    assert s.is_resumable == False

def test_completed_not_resumable():
    s = make_session(SessionStatus.COMPLETED)
    assert s.is_resumable == False

def test_active_is_resumable():
    s = make_session(SessionStatus.ACTIVE)
    assert s.is_resumable == True

def test_paused_is_resumable():
    s = make_session(SessionStatus.PAUSED)
    assert s.is_resumable == True

def test_failed_is_resumable():
    s = make_session(SessionStatus.FAILED)
    assert s.is_resumable == True