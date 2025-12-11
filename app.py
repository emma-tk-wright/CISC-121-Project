#Name: Emma Wright
#Student Number: 20228446
#Course: CISC 121

import gradio as gr # Import the Gradio library for building interactive web interfaces

def parse_list(input_str):
    """
    Convert a string seperated by commas like "5, 1, 8" into a list of integers [5, 1, 8].
    Make it ignore extra spaces and empty values.
    """
    try:
        # Split the input string by commas, strip whitespace from each part,
        # filter out empty strings, and convert the remaining parts to integers.
        numbers = [int(x.strip()) for x in input_str.split(",") if x.strip() != ""]
        if not numbers:
            # Raise an error if the resulting list is empty after parsing
            raise ValueError("List is empty")
        return numbers, "" # Return the list of numbers and an empty error message
    except ValueError:
        # Catch any ValueError (e.g., non-integer input or empty list case)
        return None, "Error: Please enter a list of integers separated by commas, e.g. 5, 1, 8 "


def binary_search_steps(arr, target):
    """
    Perform binary search on a sorted list and return:
    - a string explaining each step
    - the final result (found / not found)
    """
    steps = [] # Initialize a list to store the explanation steps
    low = 0 # Initialize the lower bound of the search range
    high = len(arr) - 1 # Initialize the upper bound of the search range
    step_num = 1 # Counter for step number

    # Continue searching as long as the lower bound is less than or equal to the upper bound
    while low <= high:
        mid = (low + high) // 2 # Calculate the middle index
        steps.append(
            f"Step {step_num}: low = {low}, high = {high}, mid = {mid}, arr[mid] = {arr[mid]}"
        )

        if arr[mid] == target:
            # If the middle element is the target, we found it
            steps.append(f" Target {target} found at index {mid}.")
            return "\n".join(steps) # Join all steps into a single string and return
        elif arr[mid] < target:
            # If the target is greater, search in the right half
            steps.append(
                f"Target {target} is greater than {arr[mid]} → search the RIGHT half (mid + 1 to high)."
            )
            low = mid + 1 # Adjust the lower bound
        else:
            # If the target is smaller, search in the left half
            steps.append(
                f"Target {target} is less than {arr[mid]} → search the LEFT half (low to mid - 1)."
            )
            high = mid - 1 # Adjust the upper bound

        steps.append("")  # Add a blank line between steps for readability
        step_num += 1 # Increment step counter

    # If the loop finishes, the target was not found
    steps.append(f" Target {target} was not found in the list.")
    return "\n".join(steps) # Return the steps indicating target not found


def run_binary_search(list_str, target_str):
    """
    Main function called by the Gradio interface.
    Takes string inputs, runs parsing + binary search, and returns a formatted result.
    """
    # Parse the list string into a list of integers
    numbers, error = parse_list(list_str)
    if error:
        return error # If there's a parsing error, return the error message

    # Parse the target string into an integer
    try:
        target = int(target_str)
    except ValueError:
        return "Error: Target must be an integer, e.g. 5" # Handle non-integer target input

    # Binary search requires a sorted list, so sort the parsed numbers
    sorted_numbers = sorted(numbers)

    # Create a header string with original and sorted lists
    header = f"Original list: {numbers}\nSorted list:   {sorted_numbers}\n\n"
    # Perform the binary search and get the step-by-step output
    steps_output = binary_search_steps(sorted_numbers, target)

    return header + steps_output # Combine header and steps output for the final result


# Build Gradio interface
title = "Binary Search Visualizer"
description = (
    "Enter a list of integers (comma-separated) and a target number. "
    "This app will run Binary Search on the sorted list and show each step."
)

# Use gr.Blocks for more flexible layout control in Gradio
with gr.Blocks() as demo:
    gr.Markdown(f"# {title}") # Display the title as a Markdown heading
    gr.Markdown(description) # Display the description as Markdown text

    # Arrange input components in a horizontal row
    with gr.Row():
        list_input = gr.Textbox(
            label="List of integers", # Label for the input box
            placeholder="Example: 5, 1, 8, 10, 2", # Example text for the input box
        )
        target_input = gr.Textbox(
            label="Target value", # Label for the target input box
            placeholder="Example: 7", # Example text for the target input box
        )

    run_button = gr.Button("Run Binary Search") # Button to trigger the search

    output_box = gr.Textbox(
        label="Steps", # Label for the output text area
        lines=20, # Number of lines to display
        interactive=False, # Make the output box read-only
    )

    # Define the action when the button is clicked
    run_button.click(
        fn=run_binary_search, # Function to call when button is clicked
        inputs=[list_input, target_input], # Inputs to pass to the function
        outputs=output_box, # Output component to update with the function's return value
    )

# This block is for running the Gradio app. It ensures `demo.launch()` is called
# when the script is executed directly (e.g., for local testing or in Hugging Face Spaces).
if __name__ == "__main__":
    demo.launch() # Launch the Gradio web interface
