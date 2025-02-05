<?php
session_start(); // Start the PHP session to track the user's login state

$servername = "localhost"; // Replace with your database server
$username = "root"; // Replace with your database username
$password = "gnr@754"; // Replace with your database password
$dbname = "servoz"; // Replace with your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Example login logic: Replace with database verification.
    // This should check the credentials against your database
    $sql = "SELECT * FROM user_profile WHERE user_Email = '$email' AND user_password = '$password'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Login successful: set the session variable
        $_SESSION['isLoggedIn'] = true;
        $_SESSION['email'] = $email; // You can also store other user information here
        echo "Login successful!";
        header("Location: home.html"); // Redirect to the home page or dashboard
    } else {
        echo "Invalid email or password.";
    }
}
?>
