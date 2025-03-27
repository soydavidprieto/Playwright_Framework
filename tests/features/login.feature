# tests/features/login.feature
Feature: Login

  Scenario Outline: Usuario válido puede acceder al sistema
    Given que el usuario accede a la página de login
    When ingresa el usuario "<username>" y la contraseña "<password>"
    Then debería ver el dashboard

  Examples:
    | username | password  |
    | Admin    | Admin123  |