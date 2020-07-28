from pytest import fixture


@fixture
def explorer():
	from pyjre.explorer import Explorer
	return Explorer()

def test_search(explorer):
	assert explorer.search(keyword="ben")['success']
		
def test_latest_podcasts(explorer):
	assert explorer.latest_podcasts()['success']
