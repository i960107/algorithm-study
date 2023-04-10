function solution(n, s, a, b, fares) {
  const graph = [];

  // graph 배열 초기화, 인접 행렬로 표현
  for (let i = 0; i < n; i++) {
    graph[i] = [];
    for (let j = 0; j < n; j++) {
      graph[i][j] = i === j ? 0 : Infinity; // 대각선 값은 0으로, 나머지는 Infinity로 초기화
    }
  }

  // graph 배열에 각 노드의 거리를 저장
  fares.forEach(([start, end, cost]) => {
    graph[start - 1][end - 1] = cost;
    graph[end - 1][start - 1] = cost;
  });

  // 플로이드-와샬 알고리즘을 이용해 모든 노드로의 최단 거리를 구함
  const distances = floydWarshall(graph);

  // 정답 초기화
  let answer = distances[s - 1][a - 1] + distances[s - 1][b - 1];

  // 합승을 고려한 최단 거리를 구함
  for (let i = 0; i < n; i++) {
    answer = Math.min(
      answer,
      distances[s - 1][i] + distances[i][a - 1] + distances[i][b - 1]
    );
  }

  return answer;
}

function floydWarshall(graph) {
  // graph: 인접 행렬
  const dist = [];
  const n = graph.length;

  // dist 배열 초기화
  for (let i = 0; i < n; i++) {
    dist[i] = [];
    for (let j = 0; j < n; j++) {
      dist[i][j] = graph[i][j];
    }
  }

  // 플로이드-와샬 알고리즘 수행
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        if (dist[i][j] > dist[i][k] + dist[k][j]) {
          dist[i][j] = dist[i][k] + dist[k][j];
        }
      }
    }
  }

  return dist;
}
