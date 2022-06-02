let width = 960,
    height = 500;

let links = [],
    nodes = [];

function initGraph(_nodes) {
    nodes = _nodes;
    d3.forceSimulation(nodes)
        .force('charge', d3.forceManyBody().strength(-100))
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
