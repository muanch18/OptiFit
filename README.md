# OptiFit Library
This project provides an object-oriented library designed for the optimization of mathematical functions. The library is designed to be easily extensible with different model functions and optimization techniques, while keeping the driver code unchanged.

## Features
- Object-oriented design using abstract base classes for Model Functions and Optimization Techniques.
- Simple interface for optimizing various mathematical models with different optimization algorithms.
- Easy addition of new models and optimization techniques with a factory pattern.
- Command-line interface to read parameters from a YAML file.

## Included Models
 - Linear Regression (LinearRegression)
 - Exponential Decay (ExponentialDecay)

## Included Optimization Techniques
- Stochastic Gradient Descent (StochasticGradientDescent)
- Genetic Algorithm (GeneticAlgorithm)

## Dependencies
- Python 3.6+
- NumPy
- SciPy
- PyYAML
- Sphinx

## Usage
- Install Dependencies
```
pip install numpy scipy matplotlib PyYAML sphinx
```
- Run the driver code with a YAML parameter file:
```
python optifit.py <parameter_file.yml>
```

## Adding New Models, Optimization Techniques, and Metrics
To add a new model:
- Create a new Python file for your model **my_model.py**
- Define a new class that inherits from the **FuncFamily** abstract base class and implement the **func()** method
- Add the new model to the **FuncFactory** class in **funcFactory.py**

To add a new optimization technique:
- Create a new Python file for your technique (e.g., **my_technique.py**)
- Define a new class that inherits from the **OptimizationTechnique** abstract base class and implement the **optimize()** method
- Add the new technique to the **OptimizationTechniqueFactory** class in **optimizationTechniqueFactory.py**

To add a new metric:
- Create a new Python file for your metric **my_metric.py**
- Define a new class that inherits from the **Metric** abstract base class and implement the **func()** method
- Add the new metric to the **MetricFactory** class in **metricFactory.py**


## Documentation
This project uses Sphinx to generate documentation from the source code.

To build the documentation, navigate to the docs/directory and run:

```
make html
```

This will generate HTML documentation in the `_build/html/` directory. Open `_build/html/index.html` in a web browser to view the documentation.

To generate a PDF of the documentation, you need to have latex and pdflatex installed. Then, you can run:

```
make latexpdf
```

This will generate a PDF file in the `_build/latex/` directory. 

Keep the Sphinx build directory (`_build/`) out of your version control system by adding it to `.gitignore`.

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/8Z1lxzU_)
