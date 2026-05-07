using System;
using System.Security.Cryptography;
using System.Text;
using Serilog;

class Program
{
    static void Main()
    {
        // Настройка логирования
        string template = "{Timestamp:HH:mm:ss} | [{Level:u3}] | {Message:lj}{NewLine}{Exception}";
        Log.Logger = new LoggerConfiguration()
            .MinimumLevel.Debug()
            .WriteTo.Console(outputTemplate: template)
            .WriteTo.File("logs/log_.txt", outputTemplate: template, rollingInterval: RollingInterval.Day)
            .CreateLogger();

        Log.Information("Приложение запущено");

        // Тестируем разные случаи
        Console.WriteLine("=== НАЧАЛО ТЕСТИРОВАНИЯ ===\n");

        TestRegistration("user@example.com", "Пароль1!", "Пароль1!");
        TestRegistration("admin", "Пароль1!", "Пароль1!");
        TestRegistration("user123", "Пароль1!", "Пароль2!");
        TestRegistration("+7-999-123-4567", "Aa1!", "Aa1!");
        TestRegistration("testuser", "КорректныйПароль123!", "КорректныйПароль123!");

        Console.WriteLine("\n=== ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ===");
        
        // Завершаем логирование
        Log.CloseAndFlush();
        
        Console.WriteLine("\nНажми любую клавишу для выхода...");
        Console.ReadKey();
    }

    static void TestRegistration(string login, string password, string confirm)
    {
        string maskedPass = MaskPassword(password);
        string maskedConfirm = MaskPassword(confirm);

        var result = UserRegistration.ValidateRegistration(login, password, confirm);

        if (result.success)
        {
            Log.Information($"✅ УСПЕХ | Логин: {login} | Пароль: {maskedPass} | Подтверждение: {maskedConfirm}");
            Console.WriteLine($"✅ Успешная регистрация: {login}");
        }
        else
        {
            Log.Error($"❌ ОШИБКА | Логин: {login} | Пароль: {maskedPass} | Подтверждение: {maskedConfirm} | Причина: {result.message}");
            Console.WriteLine($"❌ Ошибка регистрации {login}: {result.message}");
        }
    }

    static string MaskPassword(string password)
    {
        using var sha256 = SHA256.Create();
        byte[] hash = sha256.ComputeHash(Encoding.UTF8.GetBytes(password));
        return Convert.ToHexString(hash)[..8]; // первые 8 символов хеша
    }
}