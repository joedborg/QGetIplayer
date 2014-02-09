#ifndef QGETIPLAYER_H
#define QGETIPLAYER_H

#include <QMainWindow>

namespace Ui {
class QGetIplayer;
}

class QGetIplayer : public QMainWindow
{
    Q_OBJECT

public:
    explicit QGetIplayer(QWidget *parent = 0);
    ~QGetIplayer();

private:
    Ui::QGetIplayer *ui;
};

#endif // QGETIPLAYER_H
