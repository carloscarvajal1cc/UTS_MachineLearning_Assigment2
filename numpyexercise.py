{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0. 0.]\n",
      " [0. 1.]\n",
      " [0. 2.]\n",
      " [1. 0.]\n",
      " [1. 1.]\n",
      " [1. 2.]\n",
      " [2. 0.]\n",
      " [2. 1.]\n",
      " [2. 2.]]\n"
     ]
    }
   ],
   "source": [
    "##now lets learn a bit of numpy\n",
    "\n",
    "#to perform computational operations on specific part of the data \n",
    "#to run analysis or use machine learning we can use python\n",
    "#that help us storE and access data samples\n",
    "\n",
    "#numpy is a library that is designed to manage array data.\n",
    "#numpy arrays can easily be converted to/from data frames GPU\n",
    "#device arrays, images (pixel arrays), etc.\n",
    "\n",
    "#import the numpy library (as is optional)\n",
    "\n",
    "import numpy as np \n",
    "\n",
    "def function1(N):\n",
    "    \n",
    "    #Lets make an empty list\n",
    "    \n",
    "    \n",
    "    mylist = np.zeros((N**2,2))\n",
    "    index = 0\n",
    "    \n",
    "    #numpy.zeros(shape, dytype = float, order = 'C')\n",
    "    #the parameters dytype and order aren't relevant for this example\n",
    "    #we just focus on shape which is (a,b)\n",
    "    \n",
    "    #note that np.zeros((a.b)) where a is the number of observations\n",
    "    #so if a = 18, that means that you will see an array of 18\n",
    "    #observations. b on the other hand is the size of each observation\n",
    "    #in this case is 2 where so each observation will be [i.j]. if it was 3\n",
    "    #the observation will be [i.j.k]\n",
    "    \n",
    "    #numpy.zeros()\n",
    "    #the function np.zeros() returns an array with given shape and size\n",
    "    #filled with zeros.\n",
    "    \n",
    "    #with [index][] we are indicating which position in the tuple will\n",
    "    #take i and which position will take j\n",
    "\n",
    "    \n",
    "    for i in range (N):\n",
    "        for j in range (N):\n",
    "            mylist[index][0] = i\n",
    "            mylist[index][1] = j\n",
    "            index += 1\n",
    "    return mylist\n",
    "\n",
    "#now lets use an example where we call it ejemplo 1 and we assign\n",
    "# 3 as the N for the function to take\n",
    "\n",
    "\n",
    "ejemplo1 = function1(3)\n",
    "print (ejemplo1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n",
      "An X-Sample[8]:[2. 2.]\n",
      "X-Attribute[0]:[0. 0. 0. 1. 1. 1. 2. 2. 2.]\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(type(ejemplo1)) # Note the type is a np-array\n",
    "# Check out a sample\n",
    "\n",
    "### this is indexing. we are replacing the value i as the index\n",
    "# for the function we already created with the parameter N=3\n",
    "#so with i = a number is indexing. so for example if i = 5. \n",
    "# and i is between [], that means we are calling the row number 5\n",
    "#of the function with N=3, and that would be [1. 2.]. \n",
    "#remember that in python with start with 0.\n",
    "\n",
    "# {} pay attention to the order of the curly brackets.\n",
    "# the first {} represents the first part of the function .format\n",
    "# and the second {}, represents the second part of the function format \n",
    "# \"{}:{}\".\".format(first part, second part)\n",
    "\n",
    "\n",
    "i = 8\n",
    "print(\"An X-Sample[{}]:{}\".format(i, ejemplo1[i]))\n",
    "# Check attribute-0 for all samples\n",
    "\n",
    "#now you can use any letter you like. these letters are different\n",
    "#from the ones you specified in the function and mean something different\n",
    "# in this case we are indexing with a variable we call j.\n",
    "#so if j = 0 that and the format we set with the function .format\n",
    "#is [j]: [:,j]\n",
    "# now, [:,j] means take from all (:) samples the attribute specified\n",
    "#by j.\n",
    "#in this case note that the indexing done by specifiying ejemplo1[:,j]\n",
    "# is saying that the first part of the [] (before the ,) is the sample\n",
    "#we want to take or appoint. so there are 9 samples we can choose from\n",
    "#the : means all, but you can you a number between 0 and 8,\n",
    "#and index the sample you want to see. the second part of the brackets\n",
    "#after the coma, means what position of the sample you want to see.\n",
    "# note that the size is 2. so you can choose position 0 (j=0), which is\n",
    "#the first number of the sample or position 1 (j=1), which is the second \n",
    "#number of the sample and print just that number and not the \n",
    "#entire sample.\n",
    "\n",
    "\n",
    "j = 0\n",
    "print(\"X-Attribute[{}]:{}\".format(j, ejemplo1[:,j]))\n",
    "# [:, 0]: take from all (:) samples, the attribute-0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'numpy.ndarray'>\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(type(ejemplo1)) # Note the type is a np-array\n",
    "# Check out a sample\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "X-Attribute[1]:[1. 2. 0. 1.]\n"
     ]
    }
   ],
   "source": [
    "#EXERCISE Please check (print out) the second (index=1)\n",
    "#attribute for samples 1-5 (exclusive).\n",
    "j = 1\n",
    "\n",
    "print(\"X-Attribute[{}]:{}\".format(j,ejemplo1[1:5,j]))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Numpy arrays provide interface to apply computations for all \n",
    "#elements. E.g. we may want to scale all elements in $X$ between \n",
    "#$[0, 1]$. Numpy arrays provide interface to apply computations for \n",
    "#all elements. Using an ordinary Python list, we need to reconstruct \n",
    "#another list to store the result, and perform the competition \n",
    "#element by element."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scale_X_to_0_1(X, N):\n",
    "    \"\"\"\n",
    "    Get a new list scaling the elements in X by 1/N.\n",
    "    \"\"\"\n",
    "    new_list = []\n",
    "    for x in X: # you can iterate over each element (a tuple in x)\n",
    "        # now x is one data sample in X, such as (0, 2)\n",
    "        new_list.append((x[0]/N, x[1]/N))\n",
    "    return new_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scale_x_to_0_1(X,N):\n",
    "    new_list = []\n",
    "    for x in X:\n",
    "        new_list.append((x[0]/N, x[1]/N))\n",
    "    return new_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "#now lets use the function we set before (not numpy, just python)\n",
    "\n",
    "def myfunction(N):\n",
    "    \n",
    "    mylist = []\n",
    "    \n",
    "    return[(i,j) for i in range (N)\n",
    "           for j in range (N)]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
     ]
    }
   ],
   "source": [
    "a= myfunction(500)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "IOPub data rate exceeded.\n",
      "The notebook server will temporarily stop sending output\n",
      "to the client in order to avoid crashing it.\n",
      "To change this limit, set the config variable\n",
      "`--NotebookApp.iopub_data_rate_limit`.\n",
      "\n",
      "Current values:\n",
      "NotebookApp.iopub_data_rate_limit=1000000.0 (bytes/sec)\n",
      "NotebookApp.rate_limit_window=3.0 (secs)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "X = myfunction(500)\n",
    "X1 = scale_x_to_0_1(X,5)\n",
    "print (X1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.   0. ]\n",
      " [ 0.   0.2]\n",
      " [ 0.   0.4]\n",
      " ...\n",
      " [99.8 99.4]\n",
      " [99.8 99.6]\n",
      " [99.8 99.8]]\n"
     ]
    }
   ],
   "source": [
    "# On the other hand, opperating in numpy is much easier.\n",
    "\n",
    "X_np = function1(500)\n",
    "X1_np = X_np/5\n",
    "print(X1_np)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "62 ms ± 1.05 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)\n"
     ]
    }
   ],
   "source": [
    "#Not only the code is more concise. \n",
    "#The computation is done internally using fast C implementation,\n",
    "#and therefore more efficient.\n",
    "\n",
    "%timeit X1 = scale_X_to_0_1(X, 5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "714 µs ± 20.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit X1 = X1_np = X_np/5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Note the time units $\\mu$s ($10^{-6}$ sec) / ns ($10^{-9}$ sec) \n",
    "#used in the measurement above. You can make a larger matrix e.g. \n",
    "#using generate_all_X_space_samples(500) and comparethe difference.\n",
    "\n",
    "#by using numpy there is less time."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 181,
   "metadata": {},
   "outputs": [],
   "source": [
    "def generate_all_X_space_samples_np(N):\n",
    "    \"\"\"\n",
    "    :param N: X-space will be an N by N discrete-valued array\n",
    "    \"\"\"\n",
    "    X0, X1 = np.meshgrid(np.arange(N), np.arange(N))\n",
    "    # We will have the following for N=3\n",
    "    # X0:      X1:\n",
    "    # 0 1 2    0 0 0\n",
    "    # 0 1 2    1 1 1\n",
    "    # 0 1 2    2 2 2\n",
    "    \n",
    "    # X0, if \"flattened\", becomes\n",
    "    # 0 1 2 0 1 2 0 1 2\n",
    "    \n",
    "    # flattened X0 and X1 if \"stacked\" becomes\n",
    "    # [[0 1 2 0 1 2 0 1 2\n",
    "    #  [0 0 0 1 1 1 2 2 2]]\n",
    "    \n",
    "    # The following matrix, \n",
    "    # [[a b c]\n",
    "    #  [d e f]]\n",
    "    # if \"transposed\" (numpy operator \"T\"), becomes\n",
    "    # [[a d]\n",
    "    #  [b e]\n",
    "    #  [c f]]\n",
    "    return np.stack([X0.flatten(), X1.flatten()]).T"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0 0]\n",
      " [1 0]\n",
      " [2 0]\n",
      " [0 1]\n",
      " [1 1]\n",
      " [2 1]\n",
      " [0 2]\n",
      " [1 2]\n",
      " [2 2]]\n"
     ]
    }
   ],
   "source": [
    "print(generate_all_X_space_samples_np(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.29 ms ± 352 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit generate_all_X_space_samples_np(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "26.2 ms ± 445 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)\n"
     ]
    }
   ],
   "source": [
    "%timeit myfunction(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Finally, we can make version that includes the normalisation \n",
    "# (1/N) in the construction\n",
    "def generate_all_X_space_normalised_samples_np(N):\n",
    "    \"\"\"\n",
    "    :param N: X-space will be an N by N discrete-valued array\n",
    "    \"\"\"\n",
    "    X0, X1 = np.meshgrid(np.arange(N), np.arange(N))\n",
    "    return np.stack([X0.flatten(), X1.flatten()]).T / N"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[0.         0.        ]\n",
      " [0.33333333 0.        ]\n",
      " [0.66666667 0.        ]\n",
      " [0.         0.33333333]\n",
      " [0.33333333 0.33333333]\n",
      " [0.66666667 0.33333333]\n",
      " [0.         0.66666667]\n",
      " [0.33333333 0.66666667]\n",
      " [0.66666667 0.66666667]]\n"
     ]
    }
   ],
   "source": [
    "print (generate_all_X_space_normalised_samples_np(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}