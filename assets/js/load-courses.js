let width = 960,
    height = 500;

let links = [],
    nodes = [];

function initGraph(_nodes) {
    let courses = [];
    let semesters = [];
    _nodes = _nodes.filter(_n => !(_n['Tárgy neve'].includes('Szakdolgozat'))
        && !(_n['Tárgy neve'].includes('Diplomamunka'))
        && !(_n['Tárgy neve'].includes('Thesis')));
    for (let _n of _nodes) {
        if (courses.findIndex(course => (course['Tárgykód'] === _n['Tárgykód'] || course['Tárgy neve'] === _n['Tárgy neve'])) === -1) {
            courses.push({..._n, 'type': 'course'});
        }
        if (semesters.findIndex(semester => semester['name'] === _n['Félév']) === -1) {
            semesters.push({
                name: _n['Félév'],
                'type': 'semester'
            });
        }
    }
    nodes = courses.concat(semesters);
    for (const [node_index, node] of nodes.entries()) {
        if (node['type'] === 'course') {
            let semester_index = nodes.findIndex(semester => semester['type'] === 'semester' && semester['name'] === node['Félév']);
            links.push({
                'source': node_index,
                'target': semester_index
            });
        }
    }
    d3.forceSimulation(nodes)
        .force('charge', d3.forceManyBody().strength(-50))
        .force('center', d3.forceCenter(width / 2, height / 2))
        .force('link', d3.forceLink().links(links))
        .on('tick', tick);
}

function updateLinks() {
    svg.selectAll('line')
        .data(links)
        .join('line')
        .attr('class', 'edge')
        .attr('x1', function(d) {
            return d.source.x
        })
        .attr('y1', function(d) {
            return d.source.y
        })
        .attr('x2', function(d) {
            return d.target.x
        })
        .attr('y2', function(d) {
            return d.target.y
        });
}

function updateNodes() {
    svg.selectAll('circle')
        .data(nodes)
        .join('circle')
        .attr('class', 'node')
        .attr('cx', function(d) {
            return d.x
        })
        .attr('cy', function(d) {
            return d.y
        })
        .attr('r', 10);
}


function tick() {
    updateLinks();
    updateNodes();
}

let svg = d3.select("svg#past-courses")
    .attr("width", width)
    .attr("height", height);

d3.csv('/assets/data/past-courses.csv').then((data) => initGraph(data));
