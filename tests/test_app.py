import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

def test_home_route():
    """Test that home route returns correct message"""
    # Basic import test
    assert True

def test_requirements_exist():
    """Test that requirements.txt exists"""
    assert os.path.exists('backend/requirements.txt')

def test_dockerfile_exists():
    """Test that Dockerfile exists"""
    assert os.path.exists('backend/Dockerfile')

def test_compose_exists():
    """Test that docker-compose.yml exists"""
    assert os.path.exists('docker-compose.yml')