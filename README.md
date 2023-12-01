# go-vs-python-sort
Comparing the execution speed of Go and Python when running a basic bubble sort algorithm

I will be comparing the execution speed of Go and Python when running a basic bubble sort algorithm. I will be using the same array of 10,000 random integers for both languages. I will use as close to the same code and logic as possible in both languages to ensure a fair comparison.

## Running Comparisons

**Note: These comparisons will take a moment, especially for Python.**

### Go
```
go run app.go
```

### Python
```
python app.py
```

## Results

You will observe that Go is much, much more efficient than Python due to being more lightweight, with low performance overhead. Go is also compiled to machine code, whereas Python is interpreted at runtime. This is why Go is much faster than Python.