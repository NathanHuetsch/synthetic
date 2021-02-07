import numpy as np

def balanced_graph(number_of_nodes, number_of_cluster):
  # create the incidence matrix A of a densely connected graph with equi-sized clusters
  # nodes in the same cluster are connected by edges with weight +1
  # nodes in different clusters are connected by edges with weight -1
  # input: int number_of_nodes, int number_of_clusters
  # output: np.array incidence matrix A
  
  assert type(number_of_nodes) == int
  assert type(number_of_clusters) == int
  assert number_of_nodes % number_of_clusters == 0
  
  cluster_size = number_of_nodes / number_of_clusters
  A = np.zeros((number_of_nodes, number_of_nodes))
  
  for i in range(number_of_clusters):
    A[i*cluster_size : (i+1)*cluster_size, i*cluster_size : (i+1)*cluster_size] = np.ones((cluster_size, cluster_size))
    
  return 2*A - 1


def general_graph(cluster_sizes):
  # create the incidence matrix A of a densely connected graph with given cluster sizes
  # nodes in the same cluster are connected by edges with weight +1
  # nodes in different clusters are connected by edges with weight -1
  # input: list or 1d-array of integer cluster sizes
  # output: np.array incidence matrix A

  assert isinstance(cluster_sizes, np.ndarray) or isinstance(cluster_sizes, list)
  if isinstance(cluster_sizes, list):
    cluster_sizes = np.array(cluster_sizes)
  
  number_of_nodes = np.sum(cluster_sizes)
  number_of_cluster = len(cluster_sizes)
  cumulative = np.cumsum(cluster_sizes)
  A = np.zeros((number_of_nodes, number_of_nodes))
  
  A [:cumulative[0], :cumulative[0]] = np.ones((cluster_sizes[0], cluster_sizes[0]))
  for c in range(1, number_of_clusters):
    A[ cumulative[c] : cumulative[c+1], cumulative[c] : cumulative[c+1] ] = np.ones((cluster_sizes[c], cluster_sizes[c]))

  return return 2*A - 1



def add_noise(A, p)
  # randomly flip some edge weights in a given graph to simulate noisy edge predictions
  # input: incidence matrix A, flip probability p
  # output: new incidence matrix
  
  assert isinstance(A, np.ndarray)
  assert type(p) == float
  assert 0 <= p and p <= 1
  
  for i in range(A.shape[0]):
    for j in range(i):
      flip = np.random.randint(low=0, high=1) < p
      A[i,j] = A[i,j] - 2*flip*A[i,j]
      A[j,i] = A[i,j]
      
  return A
      
      
      
      
  
  
