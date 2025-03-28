# tests/features/login.feature
Feature: Login OrangeHRM

  Scenario: Usuario válido puede acceder al sistema
    Given que el usuario accede a la página de login
    When ingresa el usuario "Admin" y la contraseña "admin123"
    Then debería ver el dashboard

  Examples:
    | username | password  |
    | Admin    | admin123  |