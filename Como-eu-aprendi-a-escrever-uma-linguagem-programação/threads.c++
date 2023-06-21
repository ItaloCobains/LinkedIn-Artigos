#include <iostream>
#include <thread>
#include <vector>

// Função que será executada por cada thread
void threadFunction(int threadId) {
    std::cout << "Thread " << threadId << " iniciada." << std::endl;
    // Simulação de trabalho da thread
    for (int i = 0; i < 5; ++i) {
        std::cout << "Thread " << threadId << " executando. Contador: " << i << std::endl;
    }
    std::cout << "Thread " << threadId << " finalizada." << std::endl;
}

int main() {
    const int numThreads = 3;
    std::vector<std::thread> threads;

    // Criação e inicialização das threads
    for (int i = 0; i < numThreads; ++i) {
        threads.push_back(std::thread(threadFunction, i));
    }

    // Aguarda todas as threads terminarem
    for (auto& thread : threads) {
        thread.join();
    }

    std::cout << "Todas as threads finalizadas. Encerrando o programa." << std::endl;

    return 0;
}
