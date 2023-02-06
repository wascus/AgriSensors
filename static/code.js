var cyS = [
  cytoscape({

  container: document.getElementById('cy1'), // container to render in
  
  elements: [ // list of graph elements to start with

    // nodes
    { // node a
      data: { id: '7' }
    },
    { // node b
      data: { id: '2' }
    },
    { // node c
      data: { id: '4' }
    },
    { // node e
      data: { id: '6' }
    },
    { // node f
      data: { id: '1' }
    },
    { // node g
      data: { id: '8' }
    },
    { // node i
      data: { id: '3' }
    },
    { // node j
      data: { id: '5' }
    },
    { // node k
      data: { id: '9'}
    },

    // edges
    { // edge 61
      data: { id: '61', source: '6', target: '1' }
    },
    { // edge 13
      data: { id: '13', source: '1', target: '3' }
    },

  ],
  
  style: [ // the stylesheet for the graph
    {
      selector: 'node',
      style: 
      {
        'background-color': '#bedce8',
        'label': 'data(id)',
        'text-valign': 'center',
        'text-halign': 'center',
        'color': 'black',
        'shape': 'pentagon',
        'border-color': 'black',
        'border-width': 1,
      }
    },

    {
      selector: '#2',
      style: 
      {
        // circular shape
        'shape': 'ellipse',
      }
    },
  
    {
      selector: '#61',
      style: 
      {
        'width': 3,
        'line-color': "#992ec7",
        'curve-style': 'bezier',
      }
    },

    {
      selector: '#13',
      style: 
      {
        'width': 3,
        'line-color': 'green',
        'curve-style': 'bezier',
      }
    },

    

  ],
  
  layout: {
    name: 'grid',
    rows: 3
  
  }
  
  }),


  cytoscape({

    container: document.getElementById('cy2'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'yellow',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy3'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'yellow',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy4'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'yellow',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy5'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy6'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy7'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'darkgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy8'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'darkgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': '#a6110f',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),
 
  cytoscape({

    container: document.getElementById('cy9'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'darkgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': '#a6110f',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy10'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': '#a6110f',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),

  cytoscape({

    container: document.getElementById('cy11'), // container to render in
    
    elements: [ // list of graph elements to start with
  
      // nodes
      { // node a
        data: { id: '7' }
      },
      { // node b
        data: { id: '2' }
      },
      { // node c
        data: { id: '4' }
      },
      { // node e
        data: { id: '6' }
      },
      { // node f
        data: { id: '1' }
      },
      { // node g
        data: { id: '8' }
      },
      { // node i
        data: { id: '3' }
      },
      { // node j
        data: { id: '5' }
      },
      { // node k
        data: { id: '9' }
      },
  
      // edges
      { // edge 61
        data: { id: '61', source: '6', target: '1' }
      },
      { // edge 13
        data: { id: '13', source: '1', target: '3' }
      },
      { // edge 21
        data: { id: '21', source: '2', target: '1' }
      },
      { // edge 64
        data: { id: '64', source: '6', target: '4' }
      },
      { // edge 65
        data: { id: '65', source: '6', target: '5' }
      },
      { // edge 76
        data: { id: '76', source: '7', target: '6' }
      },
      { // edge 71
        data: { id: '71', source: '7', target: '1' }
      },
    ],
    
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: 
        {
          'background-color': '#bedce8',
          'label': 'data(id)',
          'text-valign': 'center',
          'text-halign': 'center',
          'color': 'black',
          'shape': 'pentagon',
          'border-color': 'black',
          'border-width': 1,
        }
      },
  
      {
        selector: '#2',
        style: 
        {
          // circular shape
          'shape': 'ellipse',
        }
      },
    
      {
        selector: '#61',
        style: 
        {
          'width': 3,
          'line-color': "#992ec7",
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#13',
        style: 
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },
  
      {
        selector: '#21',
        style:
        {
          'width': 3,
          'line-color': 'red',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#64',
        style:
        {
          'width': 3,
          'line-color': '#a6110f',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#65',
        style:
        {
          'width': 3,
          'line-color': 'lightgreen',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#76',
        style:
        {
          'width': 3,
          'line-color': '#992ec7',
          'curve-style': 'bezier',
        }
      },

      {
        selector: '#71',
        style:
        {
          'width': 3,
          'line-color': 'orange',
          'curve-style': 'bezier',
        }
      },
    ],
    
    layout: {
      name: 'grid',
      rows: 3
    }
    
    }),
];

for (var i = 0; i < cyS.length; i++) {
  cyS[i].on('click', 'node', function(evt){
    console.log( 'clicked ' + this.id() );
  });
}
