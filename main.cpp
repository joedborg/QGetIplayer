#include "qgetiplayer.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QGetIplayer w;
    w.show();

    return a.exec();
}
