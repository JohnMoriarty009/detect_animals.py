# Simple Python Sales Tracking System 📈

Welcome to the Simple Python Sales Tracking System repository! This project is a basic command-line application built in Python to help track sales records, calculate total revenue, and export data.

## ✨ Project Description

This application provides a straightforward way to manage sales data for small-scale tracking. It uses a lightweight SQLite database to store information persistently and offers a simple command-line interface for interaction. The project demonstrates fundamental database operations (Create, Read, Calculate) and integrates with the `pandas` library for convenient data export to Excel.

## 🚀 Features

* **Add New Sales:** Record details for each sale, including customer information, product details, price, and quantity.
* **View All Sales:** Display a list of all recorded sales with all relevant details.
* **Calculate Total Revenue:** Compute and show the sum of `total_revenue` for all sales.
* **Export to Excel:** Export all sales data from the database into a neatly formatted Excel file (`.xlsx`).

## 🛠️ Technologies Used

* **Python:** The core programming language.
* **SQLite:** A serverless, file-based database used for storing sales records.
* **pandas:** A powerful data manipulation library used here specifically for exporting data to Excel.
* **openpyxl:** A library that `pandas` uses under the hood to write `.xlsx` files.

## prerequisites

Make sure you have Python installed on your system. You'll also need the `pandas` and `openpyxl` libraries. You can install them using pip:

```bash
pip install pandas openpyxl
```

## How to Use 🖱️

1.  **Clone the repository:**
    ```bash
    git clone <https://github.com/JohnMoriarty009>
    cd <https://github.com/JohnMoriarty009/sales_tracking.py>
    ```
2.  **Run the script:**
    ```bash
    python sales_tracking.py # Assuming you named your script sales_tracking.py
    ```
3.  Follow the on-screen menu to interact with the application:
    * Enter `1` to add a new sale.
    * Enter `2` to view all sales.
    * Enter `3` to calculate the total revenue.
    * Enter `4` to export data to an Excel file (`sales_export.xlsx`).
    * Enter `5` to exit the application.

## 🗺️ Project Journey: How We Built It

This project was built step-by-step:

1.  **Database Initialization:** We started by setting up the SQLite database connection and creating the `sales` table to define the structure for storing our sales records (`id`, `customer_name`, `customer_contact`, `sale_date`, `product_name`, `price`, `quantity`, `total_revenue`).
2.  **Adding Sales:** We implemented a function to insert new sales records into the database. This included calculating the `total_revenue` (`price * quantity`) automatically before saving.
3.  **Viewing Sales:** A function was created to retrieve all sales records from the database and display them in a readable, tabular format in the console.
4.  **Calculating Total Revenue:** We added functionality to query the database and calculate the sum of the `total_revenue` for all sales, providing the total income generated.
5.  **Creating the User Interface:** A simple command-line menu loop was developed to allow users to easily select and perform actions (add, view, total, export, exit) without needing to modify the code.
6.  **Exporting to Excel:** We integrated the `pandas` library to add an export feature, allowing all stored sales data to be easily saved as an `.xlsx` file.

## 🐛 Correction Made

During the development of the `view_sales` function, we specifically addressed how to handle cases where the `customer_contact` might be `None` (if the user didn't provide contact information when adding a sale). The correction ensures that instead of printing `None`, the output shows "N/A" for better readability in the sales list display.

## 🌟 Future Enhancements

Here are some ideas for future improvements:

* Add functionality to edit or delete sales records.
* Implement filtering options (e.g., view sales by date range, by customer, by product).
* Add more robust input validation.
* Develop a graphical user interface (GUI) instead of a command-line interface.
* Include reporting features (e.g., sales summaries by product or month).

##🤝 Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request!

## 📄 License

[MIT License]
```

**How to use this text:**

1.  Go to your GitHub repository page.
2.  Click on the "Add a README" button if you don't have one, or click on the `README.md` file and then the pencil icon to edit it.
3.  Copy and paste the entire text provided above into the editing area.
4.  Make sure the repository URL in the "How to Use" section is correct.
5.  Fill in the License information in the "License" section.
6.  Commit the changes.

This README should give anyone visiting your repository a clear understanding of your project! Let me know if you'd like any adjustments or further details added.
