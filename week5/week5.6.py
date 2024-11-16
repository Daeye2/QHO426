def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods) ,  max(likelihoods)



def run_task1():
   # likelihood_of_falling = likelihood()
    print(f"Minimum likelihood of falling is {min(likelihood())}%")
    print(f"Maximum likelihood of falling is {max(likelihood())}%")


if __name__ == "__main__":
        run_task1()