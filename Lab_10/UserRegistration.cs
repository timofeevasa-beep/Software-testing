using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class UserRegistration
{
    private static readonly HashSet<string> _blockedLogins = new()
    {
        "admin", "root", "user", "test", "moderator"
    };

    public static (bool success, string message) ValidateRegistration(
        string login, string password, string confirmPassword)
    {
        // Проверка логина
        if (string.IsNullOrWhiteSpace(login))
            return (false, "Логин не может быть пустым.");

        // Проверка телефона
        if (Regex.IsMatch(login, @"^\+\d-\d{3}-\d{3}-\d{4}$"))
        {
            // Валидный телефон
        }
        // Проверка email
        else if (Regex.IsMatch(login, @"^[^@]+@[^@]+\.[^@]+$"))
        {
            // Валидный email
        }
        else
        {
            // Простая строка
            if (!Regex.IsMatch(login, @"^[a-zA-Z0-9_]{5,}$"))
                return (false, "Логин должен содержать минимум 5 символов латиницы, цифр или '_'.");
        }

        if (_blockedLogins.Contains(login.ToLower()))
            return (false, "Логин запрещён (находится в чёрном списке).");

        // Проверка пароля
        if (password.Length < 7)
            return (false, "Пароль должен содержать минимум 7 символов.");

        if (!Regex.IsMatch(password, @"[А-ЯЁ]"))
            return (false, "Пароль должен содержать хотя бы одну заглавную кириллическую букву.");

        if (!Regex.IsMatch(password, @"[а-яё]"))
            return (false, "Пароль должен содержать хотя бы одну строчную кириллическую букву.");

        if (!Regex.IsMatch(password, @"\d"))
            return (false, "Пароль должен содержать хотя бы одну цифру.");

        if (!Regex.IsMatch(password, @"[!@#$%^&*()_+\-=\[\]{};':""\\|,.<>\/?]"))
            return (false, "Пароль должен содержать хотя бы один спецсимвол.");

        if (!Regex.IsMatch(password, @"^[А-Яа-яЁё0-9!@#$%^&*()_+\-=\[\]{};':""\\|,.<>\/?]+$"))
            return (false, "Пароль может содержать только кириллицу, цифры и спецсимволы.");

        // Проверка подтверждения
        if (password != confirmPassword)
            return (false, "Пароль и подтверждение не совпадают.");

        return (true, "");
    }
}