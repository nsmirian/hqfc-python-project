def calculate_twiss_after_drift(beta0, alpha0, gamma0, L):
    # Define the transformation matrix for a drift space
    drift_matrix = np.array([
        [1, -2*L, L**2],
        [0, 1, -L],
        [0, 0, 1]
    ])

    # Initial Twiss parameters vector
    twiss_initial = np.array([beta0, alpha0, gamma0])

    # Calculate the final Twiss parameters
    twiss_final = np.dot(drift_matrix, twiss_initial)

    # Unpack the results
    beta, alpha, gamma = twiss_final


# Example usage
#beta0 = 10.0  # Initial beta value
#alpha0 = 1.0  # Initial alpha value
#gamma0 = 1.0  # Initial gamma value (should be (1 + alpha0^2) / beta0 in practice)
#L = 5.0       # Length of the drift space

  #  beta, alpha, gamma = calculate_twiss_after_drift(beta0, alpha0, gamma0, L)
  #  print(f"Final Twiss parameters after a drift space of length {L}:")
  #  print(f"Beta: {beta}")
  #  print(f"Alpha: {alpha}")
  #  print(f"Gamma: {gamma}")
    return beta, alpha, gamma


    # Example usage for both x and y directions
    # Initial Twiss parameters for x direction
    beta0_x = 10.0  # Initial beta_x value
    alpha0_x = 1.0  # Initial alpha_x value
    gamma0_x = (1 + alpha0_x**2) / beta0_x  # Initial gamma_x value

    # Initial Twiss parameters for y direction
    beta0_y = 15.0  # Initial beta_y value
    alpha0_y = -1.5  # Initial alpha_y value
    gamma0_y = (1 + alpha0_y**2) / beta0_y  # Initial gamma_y value

    L = 1  # Length of the drift space

    # Calculate final Twiss parameters for x direction
    beta_x, alpha_x, gamma_x = calculate_twiss_after_drift(beta0_x, alpha0_x, gamma0_x, L)
    print(f"Final Twiss parameters for x direction after a drift space of length {L}:")
    print(f"Beta_x: {beta_x}")
    print(f"Alpha_x: {alpha_x}")
    print(f"Gamma_x: {gamma_x}")

    # Calculate final Twiss parameters for y direction
    beta_y, alpha_y, gamma_y = calculate_twiss_after_drift(beta0_y, alpha0_y, gamma0_y, L)
    print(f"Final Twiss parameters for y direction after a drift space of length {L}:")
    print(f"Beta_y: {beta_y}")
    print(f"Alpha_y: {alpha_y}")
    print(f"Gamma_y: {gamma_y}")
