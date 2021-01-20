{
 "metadata": {
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
   "version": "3.9.1-final"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.1 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "121f78976aa03e85486a70507aee9f64523949eb891d3583059c2460a20ccb38"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "You can learn to drive\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"What is your age?: \"))\n",
    "\n",
    "if age > 17 and age <60:\n",
    "    print(\"You can learn to drive\")\n",
    "elif age > 50 and age <60:\n",
    "    print (\"You can learn to drive, but better learn soon!\")\n",
    "else:\n",
    "    print(\"You cannot learn to drive\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "You entered an EVEN number\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Enter a number smaller than 10: \"))\n",
    "\n",
    "if number == 1 or number == 3 or number == 5 or number == 9:\n",
    "    print(\"You entered an ODD number\")\n",
    "else:\n",
    "    print(\"You entered an EVEN number\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Number is greater than 10\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Please enter a number:\"))\n",
    "\n",
    "if number>10:\n",
    "     print(\"Number is greater than 10\")\n",
    "else:\n",
    "    print(\"Number is smaller than 10\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "6\n"
     ]
    }
   ],
   "source": [
    "number = int(input(\"Please enter a number:\"))\n",
    "\n",
    "if number<10:\n",
    "    print(number + 1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "You have ordered a Happy Meal\n"
     ]
    }
   ],
   "source": [
    "menuOption=int(input(\"Select an option 1, 2 or 3\"))\n",
    "\n",
    "if (menuOption==1):\n",
    "   print(\"You have ordered a Happy Meal\")\n",
    "elif(menuOption==2):\n",
    "    print(\"You Have ordered a Big Mac Meal.\")\n",
    "elif(menuOption==3):\n",
    "    print(\"You have ordered a Quarter Pounder Meal.\")\n",
    "else:\n",
    "    print(\"You didn't choose the correct option\")\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Output\n"
     ]
    }
   ],
   "source": [
    "#start\n",
    "print(\"Output\")\n",
    "#end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Number less than zero\nDone\n"
     ]
    }
   ],
   "source": [
    "# start\n",
    "num = input(\"Please enter a number: \")\n",
    "num = float(num)\n",
    "if num>0:\n",
    "    print(\"Number less than zero\")\n",
    "if num<0:\n",
    "    print(\"Number less than 0\")\n",
    "print(\"Done\")\n",
    "# end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Would you like fries?\n",
      "Would you like a drink?\n",
      "Thank you for your order!\n"
     ]
    }
   ],
   "source": [
    "# start\n",
    "userMenu=input(\"Would you like a burger?\")\n",
    "\n",
    "if userMenu==(\"yes\"):\n",
    "   input(print(\"Would you like fries?\"))\n",
    "if userMenu==(\"yes\"):\n",
    "   input(print(\"Would you like a drink?\"))\n",
    "elif userMenu==(\"no\"):\n",
    "   input(print(\"Would you like a drink?\"))\n",
    "if userMenu==(\"yes\"):\n",
    "   print(\"Thank you for your order!\")\n",
    "elif userMenu==(\"no\"):\n",
    "   print(\"Thank you for your order!\")\n",
    "else:\n",
    "    print(\"Sorry, we only have burgers!\")\n",
    "#end\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "1800.0\n1620.0\n1458.0\n1312.2\n1180.98\n1062.882\n956.5938000000001\n"
     ]
    }
   ],
   "source": [
    "userNumber= int(input(\"Please enter the price of the vehicle\"))\n",
    "userNumber= (2000-10/100*2000)\n",
    "\n",
    "print(2000-10/100*2000)\n",
    "print(1800-10/100*1800)\n",
    "print(1620-10/100*1620)\n",
    "print(1458-10/100*1458)\n",
    "print(1312.2-10/100*1312.2)\n",
    "print(1180.98-10/100*1180.98)\n",
    "print(1062.882-10/100*1062.882)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "metadata": {},
   "outputs": [],
   "source": [
    "def function_1():\n",
    "    name = input(\"What is the price of the vehicle?\") \n",
    "    x = 2000-10/100*2000, 1800-10/100*1800, 1620-10/100*1620, 1458-10/100*1458, 1312.2-10/100*1312.2, 1180.9-10/100*1180.9, 1062.8-10/100*1062.8\n",
    "\n",
    "    output = x \n",
    "\n",
    "    return output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "(1800.0, 1620.0, 1458.0, 1312.2, 1180.98, 1062.8100000000002, 956.52)\n"
     ]
    }
   ],
   "source": [
    "message = function_1()\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ]
}