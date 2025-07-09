import aiosqlite
import asyncio


async def async_fetch_users(db):
    cur = await db.cursor()
    await cur.execute("SELECT * FROM users")
    return await cur.fetchall()


async def async_fetch_older_users(db):
    cur = await db.cursor()
    await cur.execute("SELECT * FROM users WHERE age > 40")
    return await cur.fetchall()


async def main():
    async with aiosqlite.connect("users.db") as db:
        users, older_users = await asyncio.gather(
            async_fetch_users(db), async_fetch_older_users(db)
        )

        print(f"all users ------------> \n {users}")
        print(f"all users older than 40 ------------> \n {older_users}")


asyncio.run(main())
