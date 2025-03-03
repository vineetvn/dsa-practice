# Big O notation

[youtube video](https://www.youtube.com/watch?v=V6mKVRU1evU&t=2s)

In this comprehensive tutorial on Big O Notation, the presenter simplifies the
concept to help viewers understand how algorithms scale with increasing data
size. Big O Notation is not just about speed; it measures how well an algorithm
performs as the input size grows. The tutorial begins with a basic example of a
cubic function (n³) and illustrates how the significant terms in an equation
determine its performance as n increases. The presenter explains various
complexities including O(1), O(n), O(n²), O(log n), and O(n log n), providing
practical coding examples and illustrating the differences in efficiency through
real-time algorithm executions. By analyzing algorithms such as linear search,
bubble sort, binary search, and quicksort, the tutorial emphasizes the
importance of understanding Big O Notation in evaluating the scalability and
efficiency of algorithms.

## Highlights

📈 Big O Notation Measures Scalability: It evaluates how the performance of an
algorithm changes with varying input sizes, rather than just its speed.

🧮 Cubic Complexity Example: The presenter illustrates a cubic algorithm (45n³ +
20n² + 19) and emphasizes how the dominant term (n³) dictates performance as n
increases.

⚡ Constant Time (O(1)): An algorithm that runs in constant time performs the
same, regardless of the data size, exemplified by appending an item to an array.

🔍 Linear Time (O(n)): Linear search demonstrates that the execution time grows
directly in proportion to the input size, as every element must be checked.

🔄 Quadratic Time (O(n²)): Bubble sort serves as an example of a quadratic
algorithm that suffers from performance issues as data size increases due to
nested iterations.

🔢 Logarithmic Time (O(log n)): The binary search algorithm efficiently narrows
down the search space by half with each iteration, showcasing superior
performance.

🚀 N Log N Complexity (O(n log n)): Quick sort exemplifies a more efficient
sorting algorithm, balancing the need to examine each element while minimizing
redundant comparisons.

## Key Insights

📊 Understanding Big O is Critical for Scalability: Big O notation is essential
for developers and computer scientists to assess how algorithms will perform
with larger datasets. It helps in selecting appropriate algorithms based on
expected input sizes, ensuring optimal performance and resource use.

🔄 Dominant Terms Are Key: In expressions like 45n³ + 20n² + 19, as n grows, the
highest-order term (n³) becomes the dominant factor. This insight allows
programmers to simplify the evaluation of complex algorithms by focusing on the
terms that significantly affect performance.

⏱️ Performance vs. Time Complexity: While measuring the execution time of
algorithms can provide insights, it does not always correlate with efficiency.
For example, the binary search can show minimal time differences even with
increased data sizes due to its logarithmic nature, emphasizing the importance
of understanding time complexity over mere execution time.

📉 Avoiding Inefficient Algorithms: The tutorial criticizes algorithms like
bubble sort with O(n²) complexity for larger datasets. Understanding these
inefficiencies helps developers avoid suboptimal solutions, guiding them towards
more effective algorithms like quicksort or mergesort which have better
average-case performance.

🔍 Real-World Applications of Different Complexities: The tutorial includes
practical coding examples that illustrate how different algorithms operate,
thereby reinforcing the theoretical concepts. It showcases how specific
algorithms (e.g., linear search, binary search) are suited for different
scenarios based on their time complexities.

🔄 Nested Iterations Lead to Poor Performance: The discussion on O(n²)
algorithms highlights how nested loops can drastically increase the number of
operations required, leading to inefficiencies. This realization is vital for
algorithm design, where reducing nested loops can lead to significant
performance improvements.

📈 Efficient Algorithms Have Lower Growth Rates: Algorithms operating in O(log
n) and O(n log n) demonstrate slower growth in execution time as input size
increases compared to O(n) and O(n²). This insight emphasizes the importance of
choosing algorithms that not only perform well for small data sets but also
scale effectively as data grows.

In summary, understanding Big O Notation is crucial for developers to evaluate
algorithms effectively. The tutorial provides a clear path through the
complexities of algorithmic analysis, equipping viewers with the knowledge
needed to make informed decisions about algorithm selection in their programming
endeavors.
