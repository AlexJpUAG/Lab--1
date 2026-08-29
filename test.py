import user_manager
import logging

logging.basicConfig(
    level = logging.DEBUG,
    filename = "test.log",
    filemode = "w"
)

if __name__ == "__main__":
    logging.info("TEST CASE 1(RF1)")

    manager = user_manager.UserManager()

    manager.add_user(1,"Alex")

    logging.info("PASS using the debugger")

    logging.info("END TEST CASE")

    logging.info("TEST CASE 3(RF2)")

    user_1 = manager.find_user(1)

    logging.info(f"The user is {user_1}")

    if user_1["name"] == "Alex":
        logging.info("PASS")
    else:
        logging.error("ERROR")

    logging.info("END TEST CASE")

    logging.info("TEST CASE 3(RF3)")

    manager.add_user(2,"Diego")
    manager.add_user(3,"Imanol")

    manager.delete_user(2)

    logging.info("PASS using the debugger")

    logging.info("END TEST CASE")

    logging.info("TEST CASE 4(RF4)")

    names = manager.get_all_names()

    if names == ["Alex", "Imanol"]:
                 logging.info("PASS")
    else:
                 logging.error(f"FAIL, the names returned are {names}")

    logging.info("END TEST CASE")

    logging.info("TEST CASE 5(RFN1)")

    for i in range(1000):
            manager.add_user(i,"Test User " + str(i))

    logging.info("PASS")

    logging.info("END TEST CASE")