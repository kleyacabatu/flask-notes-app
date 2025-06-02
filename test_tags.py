import pytest
from app import app, db, Tag, Notebook

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Create a sample notebook to link tags to
            notebook = Notebook(name="Test Notebook")
            db.session.add(notebook)
            db.session.commit()
        yield client

        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_create_tag(client):
    response = client.post('/api/tags', json={
        'name': 'Important',
        'notebook_id': 1
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Important'
    assert data['notebook_id'] == 1

def test_get_all_tags(client):
    # Create a tag first
    client.post('/api/tags', json={'name': 'Urgent', 'notebook_id': 1})

    response = client.get('/api/tags')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1

def test_get_tag_by_id(client):
    # Create the tag and store its ID
    res = client.post('/api/tags', json={'name': 'Read Later', 'notebook_id': 1})
    tag_id = res.get_json()['id']

    # Use the dynamic tag ID instead of assuming it is 1
    response = client.get(f'/api/tags/{tag_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Read Later'

def test_update_tag(client):
    client.post('/api/tags', json={'name': 'Old Name', 'notebook_id': 1})

    response = client.put('/api/tags/1', json={'name': 'New Name'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'New Name'
    
def test_delete_tag(client):
    client.post('/api/tags', json={'name': 'Delete Me', 'notebook_id': 1})

    response = client.delete('/api/tags/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Tag 1 deleted'
